/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_do_swap.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 00:00:00 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/01 05:17:49 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_sa(t_stack **a, int w)
{
	long	temp_nbr;
	long	temp_i;

	if (!a || !*a || !(*a)->next || (*a)->next == *a)
		return ;
	temp_nbr = (*a)->nbr;
	temp_i = (*a)->i;
	(*a)->nbr = (*a)->next->nbr;
	(*a)->i = (*a)->next->i;
	(*a)->next->nbr = temp_nbr;
	(*a)->next->i = temp_i;
	if (w)
		ft_putstr("sa\n");
}

void	ft_sb(t_stack **b, int w)
{
	long	temp_nbr;
	long	temp_i;

	if (!b || !*b || !(*b)->next || (*b)->next == *b)
		return ;
	temp_nbr = (*b)->nbr;
	temp_i = (*b)->i;
	(*b)->nbr = (*b)->next->nbr;
	(*b)->i = (*b)->next->i;
	(*b)->next->nbr = temp_nbr;
	(*b)->next->i = temp_i;
	if (w)
		ft_putstr("sb\n");
}

void	ft_ss(t_stack **a, t_stack **b, int w)
{
	ft_sa(a, 0);
	ft_sb(b, 0);
	if (w)
		ft_putstr("ss\n");
}
