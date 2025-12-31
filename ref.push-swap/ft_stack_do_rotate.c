/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_do_rotate.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 12:42:56 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/01 05:17:49 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_ra(t_stack **a, int w)
{
	if (!a || !*a || !(*a)->next || (*a)->next == *a)
		return ;
	*a = (*a)->next;
	if (w)
		ft_putstr("ra\n");
}

void	ft_rb(t_stack **b, int w)
{
	if (!b || !*b || !(*b)->next || (*b)->next == *b)
		return ;
	*b = (*b)->next;
	if (w)
		ft_putstr("rb\n");
}

void	ft_rr(t_stack **a, t_stack **b, int w)
{
	ft_ra(a, 0);
	ft_rb(b, 0);
	if (w)
		ft_putstr("rr\n");
}

void	ft_execute_rotate(t_stack **from, t_stack **to,
	t_count_moves *moves)
{
	while (moves->from_up > 0 && moves->to_up > 0)
	{
		ft_rr(from, to, 1);
		moves->from_up--;
		moves->to_up--;
	}
	while (moves->from_up > 0)
	{
		ft_ra(from, 1);
		moves->from_up--;
	}
	while (moves->to_up > 0)
	{
		ft_rb(to, 1);
		moves->to_up--;
	}
}
