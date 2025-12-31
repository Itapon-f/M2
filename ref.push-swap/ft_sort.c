/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 13:07:13 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 02:40:22 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	ft_sort_three_helper(t_stack **a, long f, long s, long t)
{
	if (f > s && s > t && f > t)
	{
		ft_sa(a, 1);
		ft_rra(a, 1);
	}
	else if (f < s && s > t && f < t)
	{
		ft_sa(a, 1);
		ft_ra(a, 1);
	}
}

void	ft_sort_three(t_stack **a)
{
	long	first;
	long	second;
	long	third;

	first = (*a)->nbr;
	second = (*a)->next->nbr;
	third = (*a)->next->next->nbr;
	if (first > second && second < third && first < third)
		ft_sa(a, 1);
	else if (first > second && second < third && first > third)
		ft_ra(a, 1);
	else if (first < second && second > third && first > third)
		ft_rra(a, 1);
	else
		ft_sort_three_helper(a, first, second, third);
}

static void	ft_sort_four(t_stack **a, t_stack **b)
{
	ft_pb(a, b, 1);
	ft_sort_three(a);
	ft_pa(a, b, 1);
	if ((*a)->nbr > (*a)->next->nbr)
		ft_sa(a, 1);
}

static void	ft_sort_five(t_stack **a, t_stack **b)
{
	ft_pb(a, b, 1);
	ft_pb(a, b, 1);
	ft_sort_three(a);
	while (*b)
	{
		if ((*b)->nbr < (*a)->nbr)
			ft_pa(a, b, 1);
		else if ((*b)->nbr > ft_find_max(*a))
		{
			ft_pa(a, b, 1);
			ft_ra(a, 1);
		}
		else
		{
			while ((*a)->nbr < (*b)->nbr && (*a)->next->nbr > (*b)->nbr)
				ft_ra(a, 1);
			ft_pa(a, b, 1);
		}
	}
	ft_rotate_to_min(a);
}

void	ft_sort_small(t_stack **a, t_stack **b)
{
	int	size;

	if (!a || !*a)
		return ;
	size = ft_stack_size(*a);
	if (size == 2)
	{
		if ((*a)->nbr > (*a)->next->nbr)
			ft_sa(a, 1);
	}
	else if (size == 3)
		ft_sort_three(a);
	else if (size == 4)
		ft_sort_four(a, b);
	else if (size == 5)
		ft_sort_five(a, b);
}
